from invoke import task

@task
def start_project(ctx):
    """Start new screen session for mygpo projec"""
    ctx.run("screen -dmS feedservice ./startapp_feedservice.sh")

@task
def stop_project(ctx):
    """Add ^C to session console. Causes shell script to kill subprocesses"""
    ctx.run("""screen -X -S feedservice stuff "^C" """)
