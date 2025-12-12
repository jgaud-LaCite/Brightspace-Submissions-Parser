# Brightspace-Submissions-Parser

Un outil pour extraire et organiser les soumissions téléchargées depuis Brightspace.

## Description

Ce script extrait automatiquement les fichiers ZIP et RAR des soumissions d'étudiants et organise les fichiers par étudiant. Il peut également filtrer et remonter des fichiers spécifiques selon leur extension.

## Utilisation

```bash
python3 parse_submissions.py [Path to folder] [Extension1 (Optional)] [Extension2 (Optional)] [Extension3 (Optional)] ...
```

### Exemples

Extraire toutes les soumissions:
```bash
python3 parse_submissions.py ./submissions
```

Extraire et filtrer uniquement les fichiers .py et .txt:
```bash
python3 parse_submissions.py ./submissions .py .txt
```

## Prérequis

- Python 3
- patoolib (`pip install patool`)