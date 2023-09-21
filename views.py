from Bio import SeqIO
import subprocess
import pandas as pd
import pdfkit
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'index.html')


def fastq(request):
    if request.method == "POST":
        try:
            text_file = request.FILES['fastq']
            list_1, list_2 = sequence_extract_fastq(text_file)
            if '.fastq' in text_file.name:
                y, z = fastq_files(text_file)
                print(z)

            else:
                return render(request, 'error.html')

            context = {'files': text_file, 'z': z}
            return render(request, 'success.html', context)

        except:
            text_file = ''
        context = {'files': text_file}

    return render(request, 'index.html')


def sequence_extract_fastq(fastq_file):
    # Defining empty list for the Fastq id and fastq sequence variables
    fastq_id = []
    fastq_seq = []

    # crating a backup file with original uploaded file data
    with open('media/mtb.fastq', 'wb+') as destination:
        for chunk in fastq_file.chunks():
            destination.write(chunk)

    # opening created backup file and reading
    with open('media/mtb.fastq', 'r') as fastq_file:
        # extracting multiple data in single fastq file using biopython
        for record in SeqIO.parse(fastq_file, 'fastq'):  # (file handle, file format)

            fastq_seq.append(record.seq)
            fastq_id.append(record.id)

    # returning fastq_id and fastq sequence to both call_compare_fastq and call_reference_fastq

    return fastq_id, fastq_seq


def fastq_files(sequence):
    code = subprocess.run('TB_APP/file.sh', shell=True)

    df = pd.read_csv('/media/result.csv', usecols=["sample", "drug", "susceptibility"])
    html_string = df.to_html()
    print(df)
    print(html_string)

    pdfkit.from_string(html_string, "/mtb_file.pdf")
    print("PDF file saved.")
    return code, df




