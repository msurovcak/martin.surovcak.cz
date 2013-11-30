# -*- coding: utf-8 -*-
import os, git

from jinja2 import Environment,FileSystemLoader



# Main loop
if __name__ == '__main__':

    # Get history
    repo = git.Repo('.')
    commits = repo.log(path='me.yaml')

    # Load templates
    env = Environment(loader=FileSystemLoader(os.sep.join((
                'templates',
            ))))
    template = env.get_template('my.tmpl')
    index = env.get_template('index.tmpl')

    for commit in commits:
        
        # The newest commit is index
        if commit.id == commits[0].id:
            with open(os.sep.join(('static','index.html')), 'w+') as f:
                f.write(
                    index.render(
                        commit=commit,
                    )
                )

        with open(os.sep.join(('static','%s.html' % commit.id)), 'w+') as f:
            f.write(
                template.render(
                    commits=commits,
                    current=commit,
                    content=unicode(commit.tree['me.yaml'].data, 'utf-8')
                ).encode('utf-8')
            )
        pass