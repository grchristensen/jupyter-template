from setuptools import setup


setup(
    name="{{cookiecutter.project_name}}",
    version="0.1.0",
    packages=[
        "{{cookiecutter.project_name}}",
    ],
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        # 'somepackage==1.2.0',
        # 'repo @ https://github.com/user/archive/master.zip#egg=repo-1.0.0',
        # 'anotherpackage==4.2.1'
    ],
)
