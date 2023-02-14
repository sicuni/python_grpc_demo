from __future__ import print_function

from rpc_package.hello_pb2 import HelloRequest,HelloReply
from rpc_package.hello_pb2_grpc import GreeterStub
import grpc

def run():
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = GreeterStub(channel)
        response = stub.SayHello(HelloRequest(name="test1"))
    print("client received: " + response.message)

if __name__ == "__main__":
    run()
