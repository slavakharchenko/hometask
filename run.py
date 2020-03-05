import sys
import psutil

def memory():
	virtual_memory = psutil.virtual_memory()
	swap_memory = psutil.swap_memory()

	print('\nVirtual memory:')
	for key in ['total', 'available', 'used', 'free', 'active', 'inactive', 'wired']:
		if (hasattr(virtual_memory, key)):
			print('{}: {}'.format(key, getattr(virtual_memory, key)))

	print('\nSwap memory:')
	for key in ['total', 'used', 'free', 'percent', 'sin', 'sout']:
		if (hasattr(swap_memory, key)):
			print('{}: {}'.format(key, getattr(swap_memory, key)))


def cpu():
	cpu_times = psutil.cpu_times()

	print('\nCPU times:')
	for key in ['user', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'guest', 'guest_nice']:
		if (hasattr(cpu_times, key)):
			print('{}: {}'.format(key, getattr(cpu_times, key)))



def run():
	try:
		arg = sys.argv[1]
	except IndexError:
	    print('Please, realise argument for script: mem/cpu') 
	    return

	if arg == 'cpu':
		cpu()
	elif arg == 'mem':
		memory()
	else:
		print('Error: Wrong argument, possible mem/cpu')

run()
