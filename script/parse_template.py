from pathlib import Path
from itertools import product
import os

def to_list(version_dict):
    versions = []
    for major_version, minor_version_dict in version_dict.items():
        if isinstance(major_version, str):
            versions.append(major_version)
            continue
        for minor_version, patch_versions in minor_version_dict.items():
            for patch_version in patch_versions:
                versions.append(f'v{major_version}.{minor_version}.{patch_version}')

    return versions


def parse_template(src_path, dst_path, mode='x', **kwargs):
    with open(src_path) as src, open(dst_path, mode=mode) as dst:
        for src_line in src:
            dst.write(src_line.format(**kwargs))


def parse_dockerfiles(versions, build_types):
    root_path = Path('..')
    templates = (root_path / 'template').glob('*.template')
    models = map(lambda p: os.path.splitext(os.path.basename(p))[0], templates)

    for version, model, build_type in product(versions, models, build_types):
        docker_dir = root_path / 'docker' / version / model / build_type

        if not docker_dir.exists():
            os.makedirs(docker_dir)

        parse_template(
                root_path / 'template' / (model + '.template'),
                docker_dir / 'Dockerfile',
                mode='w',
                version=version, build_type=build_type
        )


def parse_workflows(versions):
    root_path = Path('..')
    template = (root_path / 'template' / 'docker-publish.yml')
    job = (root_path / 'template' / 'docker-publish.job')

    for os in ['alpine', 'buster-slim']:
        parse_template(
                template,
                root_path / '.github' / 'workflows' / (os + '.yml'),
                mode='w',
                os=os
        )
        for version in versions:
            parse_template(
                job,
                root_path / '.github' / 'workflows' / (os + '.yml'),
                mode='a',
                os=os, version=version
            )

if __name__=='__main__':
    build_types = ['Release', 'Debug', 'RelWithDebInfo']
    
    version_dict = {
            0: {
                1: range(8),
                2: range(3),
                3: range(9),
                4: range(5),
                5: range(2),
                6: range(2),
                7: range(1)
            },
            'stable': {
            },
            'nightly': {
            }
    }

    parse_dockerfiles(to_list(version_dict), build_types)
    parse_workflows(to_list(version_dict))
