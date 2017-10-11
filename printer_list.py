__author__ = "Anton Hvornum"
__copyright__ = "Copyright 2011, Anton Hvornum under the BSD License"
__credits__ = ["Anton Hvornum"]
__license__ = "BSD License (Original)"
__version__ = "0.0.1"
__maintainer__ = "Anton Hvornum"
__email__ = "anton.feeds@gmail.com"
__status__ = "Alpha"
 
import win32print, os
 
wp = win32print
printer_types = [(wp.PRINTER_ENUM_SHARED, 'shared'), (wp.PRINTER_ENUM_LOCAL, 'local'), (wp.PRINTER_ENUM_CONNECTIONS, 'network')]
 
print_directory = wp.GetPrintProcessorDirectory()
if not 'printers' in print_directory:
        print_directory = os.path.normpath(print_directory + '/../../PRINTERS')
 
def get_printer(name = '*'):
        printer_list = {}
        for printer_type in printer_types:
                print printer_type
                for printer in win32print.EnumPrinters(printer_type[0],None,1):
                        if name == '*':
                                printer_list[printer] = win32print.OpenPrinter(printer[2])
                        elif name.lower() in printer[2].lower():
                                printer_list[printer] = win32print.OpenPrinter(printer[2])
        return printer_list
 
def GetJobList(printer):
        printer_handle = win32print.OpenPrinter(printer)
 
        job_list = win32print.EnumJobs(printer_handle,0,-1,2)
        win32print.ClosePrinter(printer_handle)
 
        return job_list
 
def getJobDetail(printer, id):
        printer_handle = win32print.OpenPrinter(printer)
 
        job_detail = win32print.GetJob(printer_handle,id,2)
        win32print.ClosePrinter(printer_handle)
 
        return job_detail
 
printer_list = get_printer(raw_input('Name of the printer you\'re looking for (blank or * for all): '))
 
for printer in printer_list:
        print 'Joblist for:',printer
        for job in GetJobList(printer[2]):
                if 'JobId' in job:
                        job_detail = getJobDetail(printer[2], job['JobId'])
                        if not 'file_path' in job_detail:
                                job_str = '00000'
                                job_str = job_str[:-len(str(job_detail['JobId']))] + str(job_detail['JobId'])
 
                                shd_file = os.path.join(str(print_directory), job_str + '.SHD')
                                spl_file = os.path.join(str(print_directory), job_str + '.SPL')
 
                                print shd_file
                                print spl_file
 
                                if os.path.isfile(shd_file) and os.path.isfile(spl_file):
                                        job_detail['file_path'] = os.path.join(str(print_directory), str(job_detail['JobId']))
                                else:
                                        job_detail['file_path'] = str(print_directory)
                        for key in job_detail:
                                print '\t', key, '::', job_detal[key]
                print '' 
