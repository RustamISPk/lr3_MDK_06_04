from owlready2 import *

onto = get_ontology("1.OWL").load()

def findBooks(authorName=None, genreName=None, audienceName=None) -> list:
    recommendations = []
    for book in onto.book.instances():
        hasAuthor = book.hasAuthor[0].name if book.hasAuthor else "Неизвестно"
        hasGenre = book.hasGenre[0].name if book.hasGenre else "Неизвестно"
        hasTargetAuditory = book.hasTargetAuditory[0].name if book.hasTargetAuditory else "Неизвестно"

        if (authorName and authorName.lower() in hasAuthor.lower()) or \
           (genreName and genreName.lower() in hasGenre.lower()) or \
           (audienceName and audienceName.lower() in hasTargetAuditory.lower()):
            recommendations.append(f"📖 {book.name} (Автор: {hasAuthor}, Жанр: {hasGenre}, Аудитория: {hasTargetAuditory})")
    return recommendations

fav_author = input("Введите любимого автора (или нажмите Enter, чтобы пропустить): ").strip()
fav_genre = input("Введите любимый жанр (или нажмите Enter, чтобы пропустить): ").strip()
fav_audience = input("Введите предпочтительную аудиторию (или нажмите Enter, чтобы пропустить): ").strip()

result = findBooks(fav_author, fav_genre, fav_audience)

if result:
    print("Вам могут понравиться эти книги:")
    for book in result:
        print(book)
else:
    print("Извините, подходящих книг не найдено.")

