import os
import time
source = ['/Users/yangxiaoyu/Documents/106002_test_JOB020.doc', '/Users/yangxiaoyu/Documents/106002_test_JOB020.doc']
target_dir = '/Users/yangxiaoyu/Documents/'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print ('Backup FAILED')
