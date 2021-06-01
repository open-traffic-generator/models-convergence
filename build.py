""" 
The following command produces these artifacts:
    - ./artifacts/openapi.yaml
    - ./artifacts/openapi.json
    - ./artifacts/otg-convergence.proto
"""
import openapiart


openapiart.OpenApiArt(
    api_files=[
        './api/info.yaml',
        './api/api.yaml'
    ], 
    protobuf_file_name='otg-convergence', 
    output_dir='./artifacts'
)
