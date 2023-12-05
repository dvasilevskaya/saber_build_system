# Get started
1. Install `python 3.12.0`
2. Install all requirements `pipenv install --dev`
3. Run application `uvicorn main:app`
4. Open browser at http://127.0.0.1:8000/docs
5. By default, application loads `yaml` files from `builds/*`
6. There is `tox` file for code style checking and running tests. Run `tox` in terminal
7. Tests can be run with `pytest .`

## PS
Additionally, default `.yaml` paths could be overriden in `.env` file
```
builds_path=/some/other/path.yaml
tasks_path=/another/path.yaml
```