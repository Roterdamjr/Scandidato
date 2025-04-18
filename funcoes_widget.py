def configurar_botao(tela):
    button_bg_color = 'blue'
    button_fg_color = 'white'

    tela.style.configure(
        "BotaoPersonalizado.TButton",
        background=button_bg_color,
        foreground=button_fg_color,
        font=('Segoe UI', 10, 'bold')
    )

    tela.style.map(
            "BotaoPersonalizado.TButton",
            background=[('active', '#0000cc')],  # Azul mais escuro quando o botão é pressionado
            foreground=[('disabled', 'gray')]
    )

    tela.style.configure("BotaoPersonalizado.TButton", background=button_bg_color, foreground=button_fg_color)
