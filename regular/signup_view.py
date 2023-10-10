from flet import *
from regular.saveuser import save_user

def SignupView(page):

    bg_image = Container(
        Image("C:/Users/User/Desktop/web123/my_bg123.jpg")
    )

    bg_text = Container(
        margin=margin.only(top=100, left=150),
        content=Text(value='Sign Up', size=55, weight=FontWeight.W_800, color=colors.WHITE)
    )


    def go_to_signin(e):
        page.go("/signin")


    bg_have_acc = Row(
        [
            TextButton(
                text='have an account?',
                on_click=go_to_signin
            )
        ]
    )


    def changemin(e):

        mix_chr = 4

        if len(get_inp1.value) >= mix_chr and len(get_inp2.value) >= mix_chr:
            statusbtn.disabled = False
        else:
            statusbtn.disabled = True
        page.update()


    get_inp1 = TextField(
            width=350,
            border_radius=35,
            border=border.all(width=350, color=colors.WHITE24),
            border_color=colors.WHITE24,
            content_padding=padding.only(left=40),
            border_width=3,
            color=colors.WHITE,
            label='Username',
            label_style=TextStyle(
                size=15,
                color='white'
            ),
            text_style=TextStyle(
                weight=FontWeight.W_500
            ),
            max_length=24,
            on_change=changemin

        )

    get_inp1body = Container(
        content=get_inp1
    )

    get_inp2 = TextField(
        width=350,
        border_radius=35,
        border=border.all(width=350, color=colors.WHITE24),
        border_color=colors.WHITE24,
        content_padding=padding.only(left=40),
        border_width=3,
        color=colors.WHITE,
        label='Password',
        label_style=TextStyle(
            size=15,
            color='white'
        ),
        text_style=TextStyle(
            weight=FontWeight.W_500
        ),
        password=True,
        max_length=18,
        on_change=changemin

    )

    get_inp2body = Container(
        content=get_inp2
    )

    def go_to_home(e):

        save_user(
            Records=(
                get_inp1.value,
                get_inp2.value
            )
        )

        page.go("/")

    statusbtn = ElevatedButton(width=130, on_click=go_to_home, disabled=True, text='Sign up', color=colors.BLUE, bgcolor=colors.BLUE_50)
    reg_button = Container(
                Container(
                    margin=margin.only(left=100),
                    content=Column(
                        [
                            statusbtn
                        ]
                    )
                )
    )


    body = Container(
        content=Column(
            [
                Stack(
                    [
                        bg_image,
                        Row(
                            [
                                Column(
                                    [
                                        Container(
                                            margin=margin.only(top=200),
                                            width=500,
                                            height=600,
                                            border=border.all(2, color='white'),

                                            content=Container(
                                                blur=Blur(10, 1),
                                                content=Column(
                                                    [
                                                        bg_text,
                                                        Column(
                                                            [
                                                                Container(

                                                                    margin=margin.only(top=60),
                                                                    content=Row(
                                                                        [
                                                                            Column(
                                                                                [
                                                                                    Stack(
                                                                                        [
                                                                                            get_inp1body,
                                                                                            Container(
                                                                                                margin=margin.only(left=8,top=8),
                                                                                                content=Icon(
                                                                                                    name=icons.PERSON,
                                                                                                    size=29,
                                                                                                    color=colors.WHITE)
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                    Container(
                                                                                        margin=margin.only(top=15),
                                                                                        content=Column(
                                                                                            [
                                                                                                Stack(
                                                                                                    [
                                                                                                        get_inp2body,
                                                                                                        Container(
                                                                                                            margin=margin.only(
                                                                                                                left=8,
                                                                                                                top=9),
                                                                                                            content=Icon(
                                                                                                                name=icons.LOCK,
                                                                                                                size=27,
                                                                                                                color=colors.WHITE)
                                                                                                        )
                                                                                                    ]
                                                                                                ),
                                                                                                Container(
                                                                                                    margin=margin.only(top=30),
                                                                                                    content=Column(
                                                                                                        [
                                                                                                            bg_have_acc,
                                                                                                            Container(
                                                                                                                margin=margin.only(top=20),
                                                                                                                content=Column(
                                                                                                                    [
                                                                                                                        reg_button
                                                                                                                    ]
                                                                                                                )
                                                                                                            )
                                                                                                        ]
                                                                                                    )

                                                                                                )
                                                                                            ]
                                                                                        )
                                                                                    )
                                                                                ]
                                                                            )
                                                                        ],
                                                                        alignment=MainAxisAlignment.CENTER,
                                                                        vertical_alignment=MainAxisAlignment.CENTER
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        )
                                    ]
                                )
                            ],
                            alignment=MainAxisAlignment.CENTER,
                            vertical_alignment=MainAxisAlignment.CENTER
                        )
                    ]
                )
            ]
        ),
    width=1920,
    height=1080
    )

    return body