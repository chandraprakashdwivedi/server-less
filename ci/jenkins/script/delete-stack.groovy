def Deploy() {
sh '''#!/bin/bash -xe
 sls remove -v
'''
}
return this;
