if __name__ == "__main__":
    with open('./urls.txt', 'w') as f:
        for i in range(1700, 1800):
            f.write(f'https://en.wikipedia.org/wiki/{i}\n')
        f.write('q')