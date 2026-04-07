import asyncio

from pymodbus.server import StartAsyncTcpServer
from pymodbus import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext, ModbusDeviceContext

async def run_server():
    # number of register to populate
    num_reg = 200
    # initializate the datastore
    device = ModbusDeviceContext(
        di = ModbusSequentialDataBlock(0, [0,1]*(num_reg//2)),
        co = ModbusSequentialDataBlock(0, [1]*num_reg),
        hr = ModbusSequentialDataBlock(0, [17]*num_reg),
        ir = ModbusSequentialDataBlock(0, [18]*num_reg)
    )

    context = ModbusServerContext(devices=device, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = "Not Allen Bradley"
    identity.ProductCode = "ABS" # A boring simulator
    identity.ProductName = "PyModbus Sim"
    identity.ModelName = "Model_1"

    server = "127.0.0.1"
    print(f"Modbus server is starting on {server}")

    try:
        await StartAsyncTcpServer(context=context, 
                    identity=identity, 
                    address = (server, 5020)
                    )
    finally: print("Modbus server has stopped")

if __name__ == "__main__":
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("Server stopped by user")