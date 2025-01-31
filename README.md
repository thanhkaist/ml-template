# The Machine Learning Project Template 




# Docker Usage

Bring up dev environment 

```bash
USER_ID=$(id -u) GROUP_ID=$(id -g) docker compose up --build -d
```

# Testing

```bash
pip install pytest
pytest 
pytest -v 
pytest test/
pytest test/test_fixture.py
```