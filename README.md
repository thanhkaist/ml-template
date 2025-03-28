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


Share docker to github 

```yaml
% Login to docker
docker login    

% commit and tag changes in running container if needed
docker commit --author "Xuan thanh" --message "Here is my comment" <CONTAINER ID> 
docker tag <IMAGE_ID> thanhcode/my_repo:v1

% push to hub
docker push thanhcode/my-repo:v1
```

## Expose Jupyter server from Docker to Host

```bash
# Inside docker do the following 
jupyter kernelspec list # python3    /usr/local/share/jupyter/kernels/python3
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root 
# The jupyter will show the URL for connect to

# In the vscode open a ipynb file
Ctr+Shift+P -> Notebook: Select Note Book kernel -> Select  Another Kernel -> Enter the URL above.-> Name the Kernel -> Done 
```

## Testing

```bash
pip install pytest
pytest 
pytest -v 
pytest test/
pytest test/test_fixture.py
```