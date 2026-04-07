import grpc
from concurrent import futures
import time
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from address.models import Address
from address.grpc_gen import address_pb2, address_pb2_grpc

class AddressServicer(address_pb2_grpc.AddressServiceServicer):
    def GetUserAddresses(self, request, context):
        user_id = request.user_id
        addresses = Address.objects.filter(user_id=user_id)
        
        address_list = address_pb2.AddressList()
        for addr in addresses:
            address_list.addresses.append(address_pb2.Address(
                id=str(addr.id),
                user_id=str(addr.user_id),
                city=addr.city,
                state=addr.state,
                zip_code=addr.zip_code
            ))
        return address_list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    address_pb2_grpc.add_AddressServiceServicer_to_server(AddressServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC Server started on port 50051")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
