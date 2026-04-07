import asyncio

async def mb_client(client, device_id, strt_mb_address, num_regs, data_type="coils"):
	try:
		connected = await client.connect()
		if connected is False:
			raise RuntimeError("Unable to connect to Modbus server")

		if data_type == "coils":
			coil_data = await client.read_coils(strt_mb_address, 
															count=num_regs,
															device_id = device_id
															)
			if coil_data.isError():
					raise RuntimeError(f"Modbus read faield: {coil_data}")
			data = coil_data.bits[:num_regs]
		
		elif data_type == "hr":
			hr_data = await client.read_holding_registers(strt_mb_address,
																			count=num_regs,
																			device_id=device_id
																		)
			if hr_data.isError():
					raise RuntimeError(f"Modbus read failed: {hr_data}")
			
			data = hr_data.registers[:num_regs]
		else:
			raise ValueError("data_type must be 'coils' or 'hr'")
	
		reg_info = {}
		for i in range(num_regs):
			if data_type == "coils":
				reg_info[str(strt_mb_address + i)] = int(data[i])
			else:
				reg_info[str(strt_mb_address + i)] = data[i]
	
		return reg_info		   
	# DEBUG
   #  except Exception as exc:
   #      raise RuntimeError(f"Connection Failed {exc!r}") from exc
	finally:
		client.close()