# The Machine Learning Project Template 


## Supported features

- [x] Run with config yaml file
- [x] Test with pytest
- [x] Document in docs folder
- [x] Formating with pre-commit
- [x] Logger with file and terminal handlers
- [ ] More


## Docker Usage

Bring up dev environment 

```bash
USER_ID=$(id -u) GROUP_ID=$(id -g) docker compose up --build -d
```

## Testing

```bash
pip install pytest
pytest 
pytest -v 
pytest test/
pytest test/test_fixture.py
```