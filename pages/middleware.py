import odoolib






# ------------------------------------------------ Exceptions ---------------------
class MyExceptionMiddleware(object):

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		return self.get_response(request)

	def process_exception(self, request, exception):
		print()
		print('jx')

		exc_type = odoolib.main.JsonRPCException

		#if not isinstance(exception, SomeExceptionType):
		if not isinstance(exception, exc_type):
			return None

		return HttpResponse('some jx message')
