ifeq ($(OS),Windows_NT)
define set_env
set PYTHONPATH=%CD% &&
endef
else
define set_env
PYTHONPATH=$$PYTHONPATH:$(pwd)
endef
endif

run:
	@uvicorn workoutapi.app.main:app --reload

create-migrations:
	@$(set_env) alembic revision --autogenerate -m "$(d)"

run-migrations:
	@$(set_env) alembic upgrade head