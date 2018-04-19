from distutils.core import setup

setup(name='SimonD3MWrapper',
    version='1.0.0',
    description='A thin client for interacting with dockerized simon primitive',
    packages=['SimonD3MWrapper'],
    install_requires=["numpy",
        "pandas",
        "requests",
        "typing",
        "Simon=1.1.0"],
    dependency_links=[
        "git+https://github.com/NewKnowledge/simon"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.simon = SimonD3MWrapper:simon'
        ],
    },
)
