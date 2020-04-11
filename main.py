import datetime

def log_into_path(path):
  def logger_decor(old_foo):
    def new_foo(*args, **kwargs):
      log = open(path, 'w')
      output = []
      date = str(datetime.datetime.today())+'\n'
      output.append(date)
      something = old_foo(*args, **kwargs)
      name = f'{old_foo}'+'\n'
      output.append(name)
      args = str(args)+'\n'
      output.append(args)
      kwargs = str(kwargs)+'\n'
      output.append(kwargs)
      result = str(something)+'\n'
      output.append(result)
      for line in output:
        log.write(line)
      log.close()
      return something
    return new_foo
  return logger_decor

@log_into_path('log.txt')
def say_hello(name):
  hello = f'Hello, {name}'
  return hello

say_hello('Polly')