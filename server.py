from concurrent import futures
import time
import grpc
from rpc_package.hello_pb2_grpc import add_GreeterServicer_to_server,GreeterServicer
from rpc_package.hello_pb2 import HelloRequest,HelloReply


class Hello(GreeterServicer):
    def SayHello(self, request, context):
        return HelloReply(message='server:Hello, {}'.format(request.name))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Hello(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
