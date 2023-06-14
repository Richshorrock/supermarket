import file_two

print(f"file one __name__ is set to: {__name__}")

if __name__ == "__main__":
    print('file one executed directly')
else:
    print('file one was imported')