#!/bin/bash
set +e  # Continue on errors

COLOR_BLUE="\033[0;94m"
COLOR_GREEN="\033[0;92m"
COLOR_RESET="\033[0m"

# Print useful output for user
echo -e "${COLOR_BLUE}
     %########%      
     %###########%       ____                 _____                      
         %#########%    |  _ \   ___ __   __ / ___/  ____    ____   ____ ___ 
         %#########%    | | | | / _ \\\\\ \ / / \___ \ |  _ \  / _  | / __// _ \\
     %#############%    | |_| |(  __/ \ V /  ____) )| |_) )( (_| |( (__(  __/
     %#############%    |____/  \___|  \_/   \____/ |  __/  \__,_| \___\\\\\___|
 %###############%                                  |_|
 %###########%${COLOR_RESET}
Welcome to VMock development container!
This is how you can work with it:
- Single way sync between your local machine and this container.
- Some ports will be forwarded, so you can access this container via localhost.
"

# Set terminal prompt
export PS1="\[${COLOR_BLUE}\]devspace\[${COLOR_RESET}\] ./\W \[${COLOR_BLUE}\]\\$\[${COLOR_RESET}\] "
if [ -z "$BASH" ]; then export PS1="$ "; fi

# https://jichu4n.com/posts/debug-trap-and-prompt_command-in-bash/
cat <<EOT > /etc/.devspacerc
AT_PROMPT=1
function PreCommand() {
  if [ -z "\$AT_PROMPT" ]; then
    return
  fi
  unset AT_PROMPT
  if [ -f "\$DEVSPACE_WORKING_DIR/.env" ]; then
    source "\$DEVSPACE_WORKING_DIR/.env" >/dev/null
    set -a
  fi
}
trap "PreCommand" DEBUG

function PostCommand() {
  AT_PROMPT=1
}
PROMPT_COMMAND="PostCommand"
alias uwsgi="pkill -9 uwsgi && uwsgi --ini uwsgi.ini &"
EOT

# Open shell
bash --rcfile /etc/.devspacerc