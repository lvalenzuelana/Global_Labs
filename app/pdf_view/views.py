import os
from django.shortcuts import render,redirect
from teacher.models import papers
import ftplib
from django.http.response import HttpResponse
from django.http import FileResponse
# → Display search results by title. Here you can implement the rest of the searches within the database.
def pdf_view(request):
    search = request.session.get('search')
    input = request.session.get('input')
    HOSTNAME =  request.session.get('HOSTNAME')
    USERNAME =  request.session.get('USERNAME')
    PASSWORD =  request.session.get('PASSWORD')
    RUTA =  request.session.get('RUTA')
    if search == 'Title':
        if papers.objects.filter(title = input).exists():
            paper = papers.objects.get(title=input)
            filename = paper.title + ".pdf"
            ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
            ftp_server.encoding = "utf-8"
            ftp_server.cwd(RUTA)
            # → Make a copy of the paper to be able to navigate to the user in the specific directory. Please change this path to your own. 
            local_filename = os.path.join(r"/home/wicho/Papers/", filename)
            lf = open(local_filename, "wb")
            ftp_server.retrbinary("RETR " + filename, lf.write, 8*1024)
            lf.close()
            ftp_server.quit()
            return FileResponse(open("/home/wicho/Papers/"+filename, 'rb'), content_type='application/pdf')
    return redirect('/student/student')