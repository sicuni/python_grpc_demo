# python_grpc_demo

#### 编译proto:
```angular2html
python -m grpc_tools.protoc -I./proto --python_out=./rpc_package/ --grpc_python_out=./rpc_package/ .\proto\hello.proto
```
