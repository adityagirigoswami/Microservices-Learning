import grpc
from .grpc_gen import address_pb2, address_pb2_grpc
import os
from django.conf import settings

class AddressServiceClient:
    # REST fallback (optional, if you still want to support it)
    REST_URL = os.getenv("ADDRESS_SERVICE_URL", "http://localhost:8001")
    # gRPC endpoint
    GRPC_TARGET = os.getenv("ADDRESS_GRPC_TARGET", "localhost:50051")

    @classmethod
    def get_user_addresses(cls, user_id):
        """
        Fetches addresses via gRPC.
        """
        try:
            channel = grpc.insecure_channel(cls.GRPC_TARGET)
            stub = address_pb2_grpc.AddressServiceStub(channel)
            
            response = stub.GetUserAddresses(address_pb2.UserRequest(user_id=str(user_id)), timeout=5)
            
            # Convert protobuf list to a list of dicts for JSON serialization
            return [
                {
                    "id": addr.id,
                    "user_id": addr.user_id,
                    "city": addr.city,
                    "state": addr.state,
                    "zip_code": addr.zip_code
                }
                for addr in response.addresses
            ]
        except grpc.RpcError as e:
            print(f"gRPC Error connecting to Address Service: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error in AddressServiceClient: {e}")
            return None
