""" 
The following command produces these artifacts:
    - ./artifacts/openapi.yaml
    - ./artifacts/openapi.json
    - ./artifacts/otg-convergence.proto
"""
import openapiart


openapiart.OpenApiArt(
    api_files=["./api/info.yaml", "./api/api.yaml"],
    python_module_name="otg_convergence",
    protobuf_file_name="otg_convergence",
    protobuf_package_name="otg.convergence",
    output_dir="./artifacts",
)
