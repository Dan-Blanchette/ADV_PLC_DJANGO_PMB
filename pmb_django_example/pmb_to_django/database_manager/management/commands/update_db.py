from pymodbus.client import AsyncModbusTcpClient
from django.core.management.base import BaseCommand
from ...models import PLC_Tags
from ...pmb_client import mb_client
import pandas as pd
import asyncio

DEVICE_ID = 1

class Command(BaseCommand):

    def handle(self, *args, **options):
        asyncio.run(self.run_modbus())

    async def run_modbus(self):
        reg_types = ["coils", "hr"]
        mb_start_address = 0
        coils_to_read = 10
        hr_to_read = 10
        index = []


        plc_client = AsyncModbusTcpClient("127.0.0.1", port=5020)
        coil_data = await mb_client(plc_client, DEVICE_ID, mb_start_address, coils_to_read, reg_types[0])


        plc_client = AsyncModbusTcpClient("127.0.0.1", port=5020)
        hr_data = await mb_client(plc_client, DEVICE_ID, mb_start_address, hr_to_read, reg_types[1])
        

        # SAVE COIL DATA
        await PLC_Tags.objects.acreate(
            reg_type = 0,
            data=coil_data
        )

        # SAVE HOLDING REGISTER DATA
        await PLC_Tags.objects.acreate(
            reg_type = 1,
            data=hr_data
        )

        

        # # we assign our information the tags and values JSONField()
        # # tags_and_values
        # await PLC_Tags.objects.acreate(tags_and_values=db_entries)

        # self.stdout.write(
        #     self.style.SUCCESS(f"Saved PLC data: {db_entries}")
        # )