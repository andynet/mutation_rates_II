import argparse


def main():
    parser = argparse.ArgumentParser(description='Prepare input for shapeit')
    parser.add_argument('--vcf', required=True)
    parser.add_argument('--prefix', required=True)
    args = parser.parse_args()




if __name__ == '__main__':
    main()