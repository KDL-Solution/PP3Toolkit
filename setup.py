import setuptools

def load_requirements(filename='requirements.txt'):
    """Load requirements from a requirements file."""
    with open(filename, 'r') as file:
        requirements = file.read().splitlines()
        requirements = [r.strip() for r in requirements if r.strip() and not r.startswith('#')]
    return requirements

# 안전하게 README 파일 읽기
def read_long_description():
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Long description could not be read from README.md"
    
setuptools.setup(
    name="pp3_toolkit", # 모듈 이름
    version="0.0.1", # 버전
    packages = setuptools.find_packages(), # 모듈을 자동으로 찾아줌
    author="Kai", # 제작자
    author_email="koreadeep19@gmail.com", # contact
    description="koreadep play-polyground api toolkit", # 모듈 설명
    long_description=read_long_description(), # README.md에 보통 모듈 설명을 해놓는다.
    long_description_content_type="text/markdown",
    url="https://github.com/KDL-Solution/PP3Toolkit",
    install_requires=load_requirements(),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    package_data={'pp3_toolkit': ['LICENSE.txt', 'requirements.txt']},
    include_package_data=True,
    python_requires=">=3.8"
)