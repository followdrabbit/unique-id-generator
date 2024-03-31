import hashlib
import argparse

def hash_to_code(document_name):
    hasher = hashlib.sha256()
    with open(document_name, 'rb') as file:
        content = file.read()
    hasher.update(content)
    digest = hasher.digest()

    num = int.from_bytes(digest[:6], 'big')
    chars = '0123456789ABCDEF'
    code = ''.join(chars[(num >> (4 * i)) & 0xF] for i in range(11, -1, -1))
    
    formatted_code = '-'.join(code[i:i+4] for i in range(0, 12, 4))

    return hasher.hexdigest(), formatted_code

def code_to_hash(document_name, code):
    code = code.replace('-', '')
    num = int(code, 16)

    with open(document_name, 'rb') as file:
        content = file.read()

    hasher = hashlib.sha256()
    hasher.update(content)
    original_hash = hasher.hexdigest()

    return original_hash, num == int.from_bytes(hasher.digest()[:6], 'big')

def main():
    parser = argparse.ArgumentParser(description='Generate and reverse a unique code based on the document hash')
    parser.add_argument('document_name', type=str, help='Name of the document file')
    parser.add_argument('--code', type=str, help='Unique code to reverse to the original hash (optional)')

    args = parser.parse_args()

    document_name = args.document_name

    if args.code:
        original_hash, match = code_to_hash(document_name, args.code)
        print(f'Hash do documento: {original_hash}')
        if match:
            print("O código fornecido corresponde ao hash do documento.")
        else:
            print("O código fornecido NÃO corresponde ao hash do documento.")
    else:
        original_hash, code = hash_to_code(document_name)
        print(f'Hash do documento: {original_hash}')
        print(f'Código gerado: {code}')

if __name__ == '__main__':
    main()
