import file_one

print(f"file two __name__ is set to: {__name__}")

if __name__ == "__main__":
    print('file two executed directly')
else:
    print('file two was imported')