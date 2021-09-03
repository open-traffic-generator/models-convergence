""" 
The following command produces these artifacts:
    - ./artifacts/openapi.yaml
    - ./artifacts/openapi.json
    - ./artifacts/otg-convergence.proto
"""
import openapiart


openapiart.OpenApiArt(
    api_files=["./api/info.yaml", "./api/api.yaml"],
    protobuf_name="otg.convergence",
    artifact_dir="./artifacts",
).GeneratePythonSdk(package_name="otg_convergence")
