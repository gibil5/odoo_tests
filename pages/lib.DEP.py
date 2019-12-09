


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
