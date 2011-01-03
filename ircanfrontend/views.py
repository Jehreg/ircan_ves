# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
import commands

vservers = [ { 'id' : 1, 'name' : 'vserver1', 'IP' : '10.1.30.21' },
             { 'id' : 2, 'name' : 'vserver2', 'IP' : '10.1.30.22' },
             { 'id' : 3, 'name' : 'san1',     'IP' : '10.1.30.10' } ]

@login_required

def index(request):
    ves = []
    for vserver in vservers:
       raw_ves = commands.getoutput('ssh root@%s vzlist -a' % vserver['IP']).split('\n')
       del raw_ves[0]
       for raw_ve in raw_ves:
          items = raw_ve.split()
          ve = { 'veid' : int(items[0]), 'description' : items[4], 'status': items[2], 'processes': items[1], 'hostid' : vserver['id'], 'hostname' : vserver['name'] }
          ves.append(ve)

    return render_to_response('ircanfrontend/list.html', { 'ves': ves })

def reboot(request, veid, hostid):
#       result = commands.getoutput('ssh root@%s vzctl restart %s' % (vservers[int(hostid)-1]['IP'],veid))
    return redirect('/ircan')

def start(request, veid, hostid):
#       result = commands.getoutput('ssh root@%s vzctl start %s' % (vservers[int(hostid)-1]['IP'],veid))
    return redirect('/ircan')

def stop(request, veid, hostid):
#       result = commands.getoutput('ssh root@%s vzctl stop %s' % (vservers[int(hostid)-1]['IP'],veid))
    return redirect('/ircan')
