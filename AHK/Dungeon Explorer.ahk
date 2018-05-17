#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

current_weapon := 1
*+space::
    current_weapon := Mod(current_weapon, 2)
    current_weapon := current_weapon + 1

    Send, {Space down}
    Sleep, 50
    Send, {Space up}

    Send, {%current_weapon% down}
    Sleep, 50
    Send, {%current_weapon% up}

Return