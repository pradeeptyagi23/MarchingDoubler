import os,random,argparse
# Function that takes the run_length , total terms and file name as an argument
# Output - write the final series to the output file limiting the file size to 100 MB
def generate_marching_doubler(run_length:int, total_terms:int, output_file:str):
    max_file_size = 100 * 1024 * 1024 # 100MB
    series = []
    pos = 0

    # Get an initial run based on the number of run length
    chunk = ''.join(str(v) for v in list(range(1, run_length)))
    chunk_len = len(chunk)

    # Run a loop till final series length reaches the total number of terms.
    while len(series) < total_terms-1:
        for pos in range(run_length):
            # Temporary run to insert the doubled term into the right position. 
            uchunk = chunk[:]
            if(pos < chunk_len):
                # Insert the doubled term into the right position as long as the poition is less than the initial run length
                uchunk = uchunk[:pos+1]+chunk[pos]+chunk[pos+1:]
                if(len(series) < total_terms):
                    series.append(uchunk)
                else:
                    break

    # Write the final series to a file. Currently file size is restricted to 100 MB
    # Raise exception if file size increase the recommended size
    with open(output_file, 'w') as f:
        f.write(''.join(series))
    file_size = os.path.getsize(output_file)
    if file_size > max_file_size:
        raise Exception('File size exceeds maximum allowed size.')
    else:   
        print(f"Series file {output_file} successfully written")

if __name__ == '__main__':
    # Get runlength, terms and output file from CLI. (Useful while deploying using kubernetes) 
    # If any of it is not provided, prompt the user for it.
    parser = argparse.ArgumentParser()
    parser.add_argument('--runlen', help='Enter run length')
    parser.add_argument('--terms', help='Enter total number of terms')
    parser.add_argument('--ofile', help='Enter output file name')
    args = parser.parse_args()

    if args.runlen:
        runlen = int(args.runlen)
    else:
        runlen = int(input('Run length: '))

    if args.terms:
        totalterms = int(args.terms)
    else:
        totalterms = int(input('No. of terms: '))

    if args.ofile:
        outputfile = args.ofile
    else:
        outputfile = input('Output file name: ')
    dirpath = os.getcwd()
    outputfilepath = os.path.join(dirpath,outputfile)

    generate_marching_doubler(runlen, totalterms, outputfilepath)
