from flet import *


def HomeView(page):
    import sqlite3

    background = Image(
        "C:/Users/User/Desktop/web123/my_bg123.jpg"
    )

    page_home = Container(
        margin=margin.only(top=960, left=10),
        content=Row(
            [
                Text(
                    value='page Home'
                )
            ],
            alignment=alignment.bottom_left,
            vertical_alignment=alignment.bottom_left
        )
    )

    body_task = Container(
        margin=margin.only(top=80, left=130),
        content=Column(
            [
                Text(value='Какую задачу добавить?', size=45, weight=FontWeight.W_700, color='white')
            ]
        )
    )


    def add_task_click(e):

        def disable_show(e):
            txt1.value = edit_txt.value
            edit_txt.value = ''
            edit.visible = False
            page.update()

        edit_txt = TextField(
                        border='NONE',
                        text_style=TextStyle(
                            weight=FontWeight.W_500,
                            color='white',
                            size=20
                        ),
                        capitalization='WORDS'
                    )

        edit = Container(
            visible=False,
            margin=margin.only(top=2, right=5),
            content=Row(
                [
                    Icon(name=icons.ARROW_FORWARD, size=25, color=colors.WHITE),
                    edit_txt,
                    IconButton(icon=icons.SAVE_AS, icon_size=25, icon_color=colors.WHITE, on_click=disable_show)
                ]
            ),
            border=border.only(bottom=BorderSide(3, 'white'))
        )

        def remove_item(e):
            tasks.controls.remove(task)
            page.update()

        def add_edit(e):
            edit.visible = True
            page.update()

        txt1 = Text(value=text_body.content.value, size=25, weight=FontWeight.W_500, color=colors.WHITE)

        task = Container(
            alignment=alignment.top_left,
            margin=margin.only(top=20, left=40),
            content=Row(
                [
                    Checkbox(animate_size=25),
                    txt1,
                    Container(
                        content=Row([
                            edit,
                            IconButton(icon=icons.DELETE, icon_size=30, icon_color=colors.WHITE, on_click=remove_item),
                            IconButton(icon=icons.EDIT, icon_size=30, icon_color=colors.WHITE, on_click=add_edit)
                        ]
                        )
                    )
                ]
            )
        )
        tasks.controls.append(task)
        text_body.content.value = ''
        page.update()

    tasks = Column()

    text_body = Container(
        content=TextField(
            width=600,
            border='NONE',
            border_color=colors.WHITE,
            border_width=3,

            hint_text='Напишите задачу:',
            hint_style=TextStyle(
                weight=FontWeight.W_500,
                size=20,
                color=colors.WHITE,

            ),
            text_style=TextStyle(
                weight=FontWeight.W_500,
                color='white',
                size=20
            ),
            capitalization='WORDS',

        ), border=border.only(bottom=BorderSide(4, 'white')),
    )

    get_task = Container(
        content=Row(
            [Container(
                margin=margin.only(20),
                content=IconButton(icon=icons.ADD, icon_color=colors.WHITE, icon_size=25, on_click=add_task_click)
            ),
                text_body
            ],
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )
    )

    content = Container(
        content=Stack(
            [
                background,
                page_home,
                Container(
                    content=Row(
                        [
                            Container(
                                margin=margin.only(top=160),
                                width=800,
                                height=700,
                                border=border.all(width=2, color='white'),
                                content=Container(
                                    blur=Blur(10, 1),
                                    content=Column(
                                        [
                                        body_task,
                                        Container(
                                            margin=margin.only(top=60),
                                            content=Column(
                                                [
                                                    get_task,
                                                    tasks
                                                ]
                                            )
                                        )
                                    ])

                                )
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                )
            ]
        )
    )

    return content