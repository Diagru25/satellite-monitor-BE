import psutil

current_process = psutil.Process(30488)
print(current_process)
children = current_process.children(recursive=True)
for child in children:
    print('Child pid is {}'.format(child.pid))