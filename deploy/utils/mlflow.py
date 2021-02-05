from mlflow.tracking import MlflowClient
import deploy.exceptions

def load_model(client: MlflowClient, model_registry_name: str, stage: str,  fallback_stage: str = "Production"):
    """
    Get the  model version for the specified stage. Fallback to the production model if no model is available for the
    specified stage.
    Args:
        client (MlflowClient): client for MlFlow server
        model_registry_name (str): Name of the model in registry
        stage (str): Get the latest version of the model in the specified stage
        fallback_stage (str, optional): Fallback stage if no model is found in stage. Defaults to "Production".

    Raises:
        NoModelFoundException: No model found in the stage and fallback stage

    Returns:
        [type]: The model version object
    """
    models = client.get_latest_versions(
        model_registry_name, stages=[stage])

    if len(models) == 0:
        models = client.get_latest_versions(
            model_registry_name, stages=[fallback_stage])
        if len(models) == 0:
            raise deploy.exceptions.NoModelFoundException(
                f"No model {model_registry_name} found for stage {stage}  and for fallback stage {fallback_stage}")

    return models[0]
