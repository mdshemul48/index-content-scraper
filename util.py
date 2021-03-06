from guessit import guessit


def create_series_publish_table(folders: list) -> str:
    series_pub_code = "[su_tabs]"
    for folder in folders:
        series_full_title = folder["title"]
        try:
            series_obj = guessit(series_full_title)
            name = series_obj["title"]
            season = series_obj["season"]
            series_pub_code += f'\n[su_tab title="season {str(season)}" disabled="no" anchor="" url="" target="blank" class="btnplayvid"]'
        except KeyError:
            series_pub_code += f'\n[su_tab title="{series_full_title}" disabled="no" anchor="" url="" target="blank" class="btnplayvid"]'

        series_pub_code += f'\n<table style="height: 247px;" width="459">'
        series_pub_code += f"\n<tr><th>Episode</th><th>Download URL</th></tr>"
        for episode in folder["items"]:
            try:
                episode_obj = guessit(episode["title"])
                series_pub_code += f"\n<tr><td>{episode_obj['title']}.S{str(episode_obj['season'])}.E{str(episode_obj['episode'])}</td><td><a href='{episode['link']}'>Download</a></td></tr>"
            except:
                series_pub_code += f"\n<tr><td>{episode['title']}</td><td><a href='{episode['link']}'>Download</a></td></tr>"
        series_pub_code += f"\n</tbody></table>"
        series_pub_code += f"\n[/su_tab]"
    series_pub_code += f"\n[/su_tabs]"

    return series_pub_code


def create_game_publish_table(folder: list) -> str:
    game_publish_code = """
    [su_tabs]
    [su_tab title="All Parts" disabled="no" anchor="" url="" target="blank" class="btnplayvid"]
    <table style="height: 247px;" width="459">
    <tbody>
    <tr>
    <th>Parts</th>
    <th>Download URL</th>
    </tr>"""

    for item in folder:
        game_publish_code += f"<tr><td>{item['title'][:-4]}</td><td><a href='{item['link']}'>Download</a></td></tr>"

    game_publish_code += """
    </tbody>
    </table>
    [/su_tab]
    [/su_tabs]"""
    return game_publish_code
