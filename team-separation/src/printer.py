import pdfkit
from PyPDF2 import PdfFileWriter, PdfFileReader

# generate html and then print pdfs
def print_challenge_pdfs(challenges):
    challenge_pdfs = []
    for challenge in challenges:
        teams = challenges[challenge]
        cname = challenge
        cname = cname.replace(' ', '')
        if '/' in challenge or '&' in challenge:
            cname = cname.replace('/', '')
            cname = cname.replace('&', '')
        f = open(get_challenge_html_filename(cname), "w")

        f.write('<!DOCTYPE html><html><head><link rel="stylesheet" type="text/css" href="../src/style.css"></head><body>')
        f.write('<h1 id="title">'+challenge+'</h1>')
        f.write('Total number of teams: '+str(len(teams))+'<br />')

        for team in teams:
            f.write('<hr>')
            f.write('<strong><p>Team Name:</strong> '+team.team_name+'<br />')
            f.write('<strong>Room:</strong> '+team.room+'<br />')
            f.write('<strong>Table:</strong> '+team.table+'<br />')
            f.write('<strong>Project Name:</strong> '+team.project_name+'<br />')
            f.write('<strong>Project Description:</strong> '+team.project_description+'<br />')
            f.write('<strong>Team Members:</strong> '+team.member_names+'</p>')

        f.write('</body></html>')
        f.close()
        pdfkit.from_file(get_challenge_html_filename(cname), get_challenge_pdf_filename(cname))
        challenge_pdfs.append(get_challenge_pdf_filename(cname))
    return challenge_pdfs

def print_general_pdfs(judge_pairs):
    general_pdfs = []
    for pair in judge_pairs:
        teams = judge_pairs[pair]
        f = open(get_general_html_filename(str(pair)), "w")

        f.write('<!DOCTYPE html><html><head><link rel="stylesheet" type="text/css" href="../src/style.css"></head><body>')
        f.write('<h1 id="title">Judge Pair '+ str(pair) +'</h1>')
        f.write('Total number of teams: '+str(len(teams))+'<br />')

        for team in teams:
            f.write('<hr>')
            f.write('<strong><p>Team Name:</strong> '+team.team_name+'<br />')
            f.write('<strong>Room:</strong> '+team.room+'<br />')
            f.write('<strong>Table:</strong> '+team.table+'<br />')
            f.write('<strong>Project Name:</strong> '+team.project_name+'<br />')
            f.write('<strong>Project Description:</strong> '+team.project_description+'<br />')
            f.write('<strong>Team Members:</strong> '+team.member_names+'</p>')

        f.write('</body></html>')
        f.close()

        pdfkit.from_file(get_general_html_filename(str(pair)), get_general_pdf_filename(str(pair)))
        print(str(pair)+'/'+str(len(judge_pairs))+' Complete')
        general_pdfs.append(get_general_pdf_filename(str(pair)))
    return general_pdfs

def print_teams_in_room(room, teams):
    print()
    print(room)
    for team in teams:
        print(team.team_name)

def merge_pdfs(file, input_paths):
    pdf_writer = PdfFileWriter()

    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open('../output/' + file, 'wb') as fh:
        pdf_writer.write(fh)

def get_challenge_html_filename(name):
    return '../challenge-html/' + name + '.html'

def get_challenge_pdf_filename(name):
    return '../challenge-pdfs/' + name + '.pdf'

def get_general_html_filename(name):
    return '../general-html/' + name + '.html'

def get_general_pdf_filename(name):
    return '../general-pdfs/' + name + '.pdf'
