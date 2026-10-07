"""Controles de formato de los .md del repo.

Uso: python3 scripts/check.py [raíz]

Para cada .md informa la cantidad de títulos ### y de bloques <details>, y avisa si:
- los <details> no están balanceados,
- hay links o imágenes rotos,
- un bloque $$...$$ o un <summary>/</details> no tiene líneas en blanco alrededor
  (sin ellas GitHub no renderiza el markdown/LaTeX de adentro),
- hay una cantidad impar de signos $,
- una fila de tabla tiene un | dentro de una fórmula (rompe la tabla).
"""
import os, re, sys, urllib.parse

root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad = 0
for dirpath, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in ('.git', 'aula-virtual', 'scripts')]
    for f in sorted(files):
        if not f.endswith('.md'):
            continue
        p = os.path.join(dirpath, f)
        txt = open(p, encoding='utf-8').read()
        rel = os.path.relpath(p, root)
        o, c = txt.count('<details>'), txt.count('</details>')
        ex = len(re.findall(r'^### ', txt, re.M))
        issues = []
        if o != c:
            issues.append(f'details {o}/{c}')
        for m in re.finditer(r'\]\(([^)\s]+)\)', txt):
            link = m.group(1)
            if link.startswith('http') or link.startswith('#'):
                continue
            target = os.path.normpath(os.path.join(dirpath, urllib.parse.unquote(link)))
            if not os.path.exists(target):
                issues.append('broken link: ' + link)
        lines = txt.split('\n')
        for i, l in enumerate(lines):
            s = l.strip()
            if s.startswith('$$') and s.endswith('$$') and len(s) > 4:
                if i > 0 and lines[i-1].strip() != '':
                    issues.append(f'L{i+1}: $$ sin línea en blanco antes')
                if i + 1 < len(lines) and lines[i+1].strip() != '':
                    issues.append(f'L{i+1}: $$ sin línea en blanco después')
            if s in ('<summary><b>Solución</b></summary>', '<summary>Solución paso a paso</summary>'):
                if i + 1 < len(lines) and lines[i+1].strip() != '':
                    issues.append(f'L{i+1}: <summary> sin línea en blanco después')
            if s == '</details>' and i > 0 and lines[i-1].strip() != '':
                issues.append(f'L{i+1}: </details> sin línea en blanco antes')
            if s.startswith('|') and s.endswith('|'):
                for m in re.finditer(r'\$([^$]+)\$', s):
                    if '|' in m.group(1):
                        issues.append(f'L{i+1}: | dentro de fórmula en tabla')
        if txt.count('$') % 2:
            issues.append('cantidad impar de $')
        print(f'{rel}: {ex} títulos ###, {o} details' + ('' if not issues else '\n   ' + '\n   '.join(issues)))
        bad += len(issues)
print('PROBLEMAS:', bad)
