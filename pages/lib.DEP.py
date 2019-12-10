# 10 Dec 2019

# Create Django Obj

		# Variables
		name = so_model.get_name(repo_id)
		date_begin = so_model.get_date_begin(repo_id)
		date_end = so_model.get_date_end(repo_id)

		date_test = get_date_corrected(so_model.get_date_test(repo_id))

		total = so_model.get_total(repo_id)
		count = so_model.get_count(repo_id)

		state = so_model.get_state(repo_id)

		#configurator = so_model.get_configurator(repo_id)


		print()
		print()
		print(name)
		print(date_begin)
		print(date_end)
		print(date_test)

		print(total)
		print(count)

		print(state)

		# Create 
		obj = ReportSaleProduct(name=name, 
								date_begin=date_begin, 
								date_end=date_end,
								date_test=date_test,

								total=total,
								count=count,

								state=state, 
		) 	

		obj.save()

		print(obj)
		print()
		print()
		print()
		
		obj_array.append(obj)







		except odoolib.main.JsonRPCException:
			print('Lib - Exception')

			etype, eval, etb = sys.exc_info()
			
			#return error(id, 100, 'Exception %s: %s' %(etype, eval))
			#return odoolib.main.JsonRPCException



			print(etype)
			print()
			print(eval)
			print()
			#print(etb)
			#print()

			#print(eval.get_message())

			#print(eval['message'])
			#print(eval['code'])
			#print(eval['data'])
			print()



		except Exception as e:
		#except odoolib.main.JsonRPCException as e:
			print('Lib - Exception')
			print('%s (%s)' % (e.message, type(e)))
