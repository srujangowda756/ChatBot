import re, json
try:
    import google.generativeai as genai
except Exception as e:
    print('IMPORT_ERROR:'+str(e))
    raise

# Try to extract API key from app.py
key = ''
try:
    with open('app.py','r',encoding='utf-8') as f:
        s = f.read()
    m = re.search(r"GOOGLE_API_KEY\s*=\s*os.getenv\([^,]+,\s*'([^']+)'\)")
    if m:
        key = m.group(1)
except Exception as e:
    pass

if not key:
    import os
    key = os.getenv('GOOGLE_API_KEY','')

print('USING_KEY:' + (key[:10] + '...' if key else '<none>'))

try:
    genai.configure(api_key=key)
except Exception as e:
    print('CONFIGURE_ERROR:'+str(e))

# Try several list methods
try:
    if hasattr(genai, 'list_models'):
        gen = genai.list_models()
        print('LIST_METHOD:genai.list_models')
        try:
            models = list(gen)
            print(json.dumps(models, default=str, indent=2))
        except TypeError:
            # Not iterable; print repr
            print('LIST_RESULT:' + str(gen))
    elif hasattr(genai, 'models'):
        try:
            models = genai.models.list()
            print('LIST_METHOD:genai.models.list')
            print(json.dumps(models, default=str, indent=2))
        except Exception as e:
            print('MODELS_LIST_ERROR:'+str(e))
    else:
        print('NO_LIST_METHOD_FOUND')
        print('GENAI_DIR:', json.dumps([k for k in dir(genai) if not k.startswith('_')]))
except Exception as e:
    print('ERROR:'+str(e))
    import traceback
    traceback.print_exc()
